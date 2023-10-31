from google.cloud.devtools import cloudbuild
from google.cloud import aiplatform


def build_image_gcp(workspace: str):
    """Build and push Docker Image to Container Registry.

    Image will be build from Dockerfile based on build.source
    The code to be executed inside image is located in main.py

    Args:
        workspace (str): workspace to build image.
    """
    # instantiate clients
    client = cloudbuild.CloudBuildClient()
    build = cloudbuild.Build()

    # define image_name
    IMAGE_NAME = f"gcr.io/[my_project]/build_args_gcp_{workspace}"

    # build source
    build.source = {
        "git_source": {
            "url": "https://github.com/arturlunardi/gcp-docker-args",
            "dir_": "src",
            "revision": "master"
        }
    }

    # build and push image
    build.steps = [
        {
            "name": "gcr.io/cloud-builders/docker",
            "args": [
                "build",
                "-t",
                IMAGE_NAME,
                "--build-arg=WORKSPACE=${_WORKSPACE}",
                "."
            ]
        },
        {
            "name": "gcr.io/cloud-builders/docker",
            "args": ["push", IMAGE_NAME]
        }
    ]

    # display build results
    build.images = [IMAGE_NAME]

    # substitution variables - in gcp, all variables must begin with underscore
    build.substitutions = {"_WORKSPACE": workspace}

    # start build
    operation = client.create_build(project_id="project_id", build=build)
    print("Building image...")

    result = operation.result()
    # print status
    print(f"Build Result: {result.status}")
