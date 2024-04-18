
Mage is an open-source, hybrid framework for transforming and integrating data. ✨

In this module, we'll use the Mage platform to author and share _magical_ data pipelines.

## Getting started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally.



Navigate to the repo:

```bash
cd mage-ai-Workflow-Orchestration
```


Now, let's build the container

```bash
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser! Voila! You're ready to get started with a new mage repository.
It will be present in your project under the name `magic-zoomcamp`.


This folder has the following structure:

```
.
├── mage_data
│   └── magic-zoomcamp
├── magic-zoomcamp
│   ├── __pycache__
│   ├── charts
│   ├── custom
│   ├── data_exporters
│   ├── data_loaders
│   ├── dbt
│   ├── extensions
│   ├── interactions
│   ├── pipelines
│   ├── scratchpads
│   ├── transformers
│   ├── utils
│   ├── __init__.py
│   ├── io_config.yaml
│   ├── metadata.yaml
│   └── requirements.txt
├── Dockerfile
├── README.md
├── dev.env
├── docker-compose.yml
└── requirements.txt
```
