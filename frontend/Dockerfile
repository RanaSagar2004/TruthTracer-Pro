# ==========================
# Stage 1: Build React app
# ==========================
FROM node:18 AS build
WORKDIR /app

# Copy package.json (and package-lock.json if present)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Build the static production files
RUN npm run build

# ==========================
# Stage 2: Serve with nginx
# ==========================
FROM nginx:alpine AS runtime
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/build /usr/share/nginx/html

# add our custom nginx conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]