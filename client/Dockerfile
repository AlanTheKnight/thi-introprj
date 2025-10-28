# Multi-stage build for Vue.js application
# Stage 1: Build the application
FROM node:22-alpine AS build

RUN apk add --no-cache python3 make g++ libc6-compat

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
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