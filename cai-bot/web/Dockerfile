FROM nginx:1.29-alpine

# Copy custom nginx configuration
COPY site.conf /etc/nginx/conf.d/default.conf

WORKDIR /usr/share/nginx/html

# Copy web files to nginx web root
COPY --chown=nginx:nginx *.html *.css *.js ./

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
