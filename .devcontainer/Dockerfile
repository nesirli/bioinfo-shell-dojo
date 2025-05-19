# Dockerfile (root of repo)
FROM mambaorg/micromamba:1.5.6

# Copy Conda configuration
COPY .condarc /root/.condarc
COPY environment.yml /tmp/environment.yml

# Create env as /opt/conda/envs/bio-core
RUN micromamba env create -f /tmp/environment.yml && \
    micromamba clean --all --yes

# Make the env the default
ENV PATH=/opt/conda/envs/bio-core/bin:$PATH \
    CONDA_DEFAULT_ENV=bio-core

# Drop into bash by default
CMD ["bash"]