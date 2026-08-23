# 1. FROM: Defines the base operating system image
FROM python:3.11-slim

# 2. ARG: A variable ONLY available during the build process
ARG BUILD_VERSION=1.0.0

# 3. ENV: Environment variables baked into the running container
ENV SECRET_MESSAGE="Hello from inside the isolated container!"
ENV BUILD_ENV=${BUILD_VERSION}

# 4. WORKDIR: Sets the working directory for all future commands
WORKDIR /app

# 5. RUN: Executes commands *during* the build phase (installing system tools)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 6. COPY: Copies files from your local computer into the container
COPY detective.py .

# 7. EXPOSE: Documents which port the app listens on (documentation only)
EXPOSE 8080

# 8. USER: Switches away from root for security best practices (creates a non-root user)
RUN useradd -m detectiveuser
USER detectiveuser

# 9. CMD: The default command executed when the container starts
CMD ["python", "detective.py"]