# Use Node.js 20 Alpine as the base image
FROM node:22-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if exists) to leverage Docker cache
COPY package*.json ./

# Install dependencies in a single RUN command to reduce layers
RUN npm install 

# Copy the rest of the application code
COPY . .

# Expose Vite's default port
EXPOSE 5173

# Start the Vite development server
CMD ["npm", "run", "dev","--", "--host", "0.0.0.0"]