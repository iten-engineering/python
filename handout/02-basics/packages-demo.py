
import pkg_resources

installed_packages = pkg_resources.working_set

for package in installed_packages:
    print(f"{package.project_name}=={package.version}")
