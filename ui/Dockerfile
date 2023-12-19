# Use an official Node runtime as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install serve globally
RUN npm install -g serve

# Copy the rest of the app files to the working directory
COPY . .

# Expose the port that the app runs on
EXPOSE 5000

# Define the command to run the app
CMD ["serve", "-s", "."]