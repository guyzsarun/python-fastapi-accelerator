# -*- mode: Python -*
SOURCE_IMAGE = os.getenv(
    "SOURCE_IMAGE", default="index.docker.io/guyzsarun/python-fastapi-web-app-source"
)
LOCAL_PATH = os.getenv("LOCAL_PATH", default=".")
NAMESPACE = os.getenv("NAMESPACE", default="dev-namespace")

k8s_custom_deploy(
    "python-fastapi-web-app",
    apply_cmd="tanzu apps workload apply -f config/workload.yaml --live-update"
    + " --local-path "
    + LOCAL_PATH
    + " --source-image "
    + SOURCE_IMAGE
    + " --namespace "
    + NAMESPACE
    + " --yes >/dev/null"
    + " && kubectl get workload python-fastapi-web-app --namespace "
    + NAMESPACE
    + " -o yaml",
    delete_cmd="tanzu apps workload delete -f config/workload.yaml --namespace "
    + NAMESPACE
    + " --yes",
    deps=["requirements.txt", "app.py"],
    container_selector="workload",
    live_update=[sync(".", ".")],
)

k8s_resource(
    "python-fastapi-web-app",
    port_forwards=["8080:8080"],
    extra_pod_selectors=[{"serving.knative.dev/service": "python-fastapi-web-app"}],
)
