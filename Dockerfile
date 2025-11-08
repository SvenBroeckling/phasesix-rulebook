FROM texlive/texlive:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies used by the build script
# (We install them explicitly to avoid needing a wheel build backend.)
COPY pyproject.toml uv.lock ./
RUN pip3 install --no-cache-dir \
        jinja2>=3.1,<4 \
        python-dotenv>=1.0,<2 \
        requests>=2.32,<3 \
        pytokens>=0.1,<1

COPY . .

ENTRYPOINT ["python3", "build"]

# Example usage:
#   Build image:   docker build -t phasesix-rulebooks .
#   Run build:     docker run --rm -e API_KEY=... -v $(pwd)/output:/app/output phasesix-rulebooks -i "phasesix" -l "de" -m "online"
#   Update data:   docker run --rm -e API_KEY=... -v $(pwd)/output:/app/output phasesix-rulebooks -u -a
