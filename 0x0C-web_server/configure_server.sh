#!/usr/bin/env bash

# Create a file /tmp/test containing the string "hello world"
echo "hello world" > /tmp/test

# Remove any backup files that might cause conflicts
rm -f /etc/nginx/sites-enabled/default.bak

# Modify the configuration of Nginx to listen on port 8080 instead of 80
sed -i 's/listen 80;/listen 8080;/g' /etc/nginx/sites-enabled/default

# Check Nginx configuration for syntax errors
nginx -t

# If the configuration test passes, reload Nginx to apply changes
if [ $? -eq 0 ]; then
    service nginx reload
    echo "Nginx configuration successfully updated and reloaded."
else
    echo "Nginx configuration test failed. Please check the configuration file for errors."
fi
