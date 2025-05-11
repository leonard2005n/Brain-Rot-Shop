# Use a specific and minimal base image
FROM python:3.11-alpine

# Set the working directory
WORKDIR /app

# Create a non-root user and group
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
# --no-cache-dir: Disables the pip cache, reducing image size.
# --upgrade pip: Ensures pip is up-to-date.
# --no-warn-script-location: Suppresses warnings about scripts installed outside of PATH.
RUN pip install --no-cache-dir --upgrade pip && \
	pip install --no-cache-dir -r requirements.txt --no-warn-script-location

# Copy the rest of the application code
COPY . .

# Change ownership of the app directory to the non-root user
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "server.py"]
