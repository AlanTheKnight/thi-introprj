# Multi-stage build for Vue.js application
# Stage 1: Build the application
FROM node:22 AS build

WORKDIR /app

# Copy package files
COPY package*.json ./

# Clean install to avoid native binding issues
RUN rm -rf node_modules package-lock.json
RUN npm install

# Copy source code
COPY . .

# Build the application (skip type checking for faster builds)
RUN npm run build-only

# Stage 2: Serve with NGINX
FROM nginx:1.29-alpine

# Copy the built application from the build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]