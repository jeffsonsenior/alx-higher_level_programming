#!/bin/bash
#takes in a URL as an arg, sends a GET request to the URL,and displays the body of the resp.
curl -sH "X-School-User-Id: 98" "$1"
