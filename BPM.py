#!/usr/bin/env python
'''
    Simple program that uses the 'bpmdetect' GStreamer plugin to detect
    the BPM of a song, and outputs that to console. 

    Requires GStreamer 1.x, PyGObject 1.x, and gst-plugins-bad
    Copyright (C) 2015 Dustin Spicuzza
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 2 as
    published by the Free Software Foundation.
'''


from __future__ import print_function
from paramiko import client

import inspect
import sys
from os import *

from gi.repository import Gst, GObject, Gio

import paramiko 
import time
#####

import socket 

def detect_bpm(uri, on_complete):

    '''
        Detects the BPM of a song using GStreamer's bpmdetect plugin
        .. note:: The plugin emits the BPM at various times during 
                  song processing, but the bpm detector accumulates
                  the results so this will only return the last
                  result.
    '''

    bpm = [None]
    def _on_message(bus, msg):

        if msg.type == Gst.MessageType.TAG:
            tags = msg.parse_tag()

            # Discard tags already set on the file

            if tags.n_tags() > 1:
                return
            
            v = tags.get_value_index('beats-per-minute', 0)
            try:
                v = float(v)
            except:
                return

            if v > 0:
                bpm[0] = v

        elif msg.type == Gst.MessageType.ERROR:

            playbin.set_state(Gst.State.NULL)
            gerror, debug_info = msg.parse_error()

            if gerror:
                on_complete(None, gerror.message.rstrip("."))

            else:
                on_complete(None, debug_info)

        elif msg.type == Gst.MessageType.EOS:
            playbin.set_state(Gst.State.NULL)
            on_complete(bpm[0], None)

    audio_sink = Gst.Bin.new('audiosink')

    # bpmdetect doesn't work properly with more than one channel, 
    # see https://bugzilla.gnome.org/show_bug.cgi?id=751457

    cf = Gst.ElementFactory.make('capsfilter')
    cf.props.caps = Gst.Caps.from_string('audio/x-raw,channels=1')

    fakesink = Gst.ElementFactory.make('fakesink')
    fakesink.props.sync = False
    fakesink.props.signal_handoffs = False

    bpmdetect = Gst.ElementFactory.make('bpmdetect')
    if bpmdetect is None:
        on_complete(None, "GStreamer BPM detection plugin not found")
        return

    audio_sink.add(cf)
    audio_sink.add(bpmdetect)
    audio_sink.add(fakesink)

    cf.link(bpmdetect)
    bpmdetect.link(fakesink)

    audio_sink.add_pad(Gst.GhostPad.new('sink', cf.get_static_pad('sink')))

    playbin = Gst.ElementFactory.make('playbin')
    playbin.props.audio_sink = audio_sink

    bus = playbin.get_bus()
    bus.add_signal_watch()
    bus.connect('message', _on_message)

    playbin.props.uri = uri
    playbin.set_state(Gst.State.PLAYING)
    
class ssh:
    client = None

    def __init__(self, address, username, password):
            # Let the user know we're connecting to the server
            print("Connecting to server.")
            # Create a new SSH client
            self.client = client.SSHClient()
            # The following line is required if you want the script to be able to access a server that's not yet in the known_hosts file
            self.client.set_missing_host_key_policy(client.AutoAddPolicy())
            # Make the connection
            self.client.connect(address, username=username, password=password)

    def sendCommand(self, command):
            # Check if connection is made previously
            if(self.client):
                stdin, stdout, stderr = self.client.exec_command(command)
                '''while not stdout.channel.exit_status_ready():
                    # Print stdout data when available
                    if stdout.channel.recv_ready():
                        # Retrieve the first 1024 bytes
                        alldata = stdout.channel.recv(1024)
                        while stdout.channel.recv_ready():
                            # Retrieve the next 1024 bytes
                            alldata += stdout.channel.recv(1024)
                        # Print as string with utf8 encoding
                        print(str(alldata))'''
                #self.client.close() 
            else:
                print("Connection not opened.")


#####


    

connection = ssh("169.254.110.225", "robot", "maker")
                       
connection.sendCommand("python3 TestDegrees.py")


Gst.init(None)
"""if len(sys.argv) != 2:
    print("Usage: %s filename\n" % sys.argv[0])
    print(inspect.cleandoc(__doc__))
    exit(1)
"""

uri = Gio.File.new_for_commandline_arg("michael.wav").get_uri()#"Nightwish_-_Storytime_audiopoisk.wav"
print("Processing file: ", uri)

def on_complete(bpm, error):
    if error is not None:
        print("ERROR:", error)
    else:
        print("BPM:", bpm)
        bpm=int(bpm)
        connection.sendCommand("echo 'maker' | sudo -S python3 write.py %i" % bpm)

    ml.quit()

detect_bpm(uri, on_complete)

ml = GObject.MainLoop()
ml.run()
