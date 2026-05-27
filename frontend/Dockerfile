# Base Node image
FROM node:20-alpine


# Set working directory
WORKDIR /app


# Copy package files
COPY package*.json ./


# Install frontend dependencies
RUN npm install


# Copy frontend code
COPY . .


# Expose Vite port
EXPOSE 5173


# Start React app
CMD ["npm", "run", "dev", "--", "--host"]