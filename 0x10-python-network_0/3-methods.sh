#!/bin/bash
# takes in a URL and dsply all HTTP methods the server will acpt.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
