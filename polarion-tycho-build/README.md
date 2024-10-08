# polarion-tycho-build

This project demonstrates build execution with Maven and Tycho that uses the target platform generated by `polarion-target-platform`.

## How to run the build
If your update site is available at http://localhost:8080/repository, executing `mvnw clean verify` (Windows) or `./mvnw clean verify` (Linux) will run the build. On success, the plugins will be available at `releng/update-site/repository/plugins`.

## Project overview
The project is structured as follows:
* `bundles` that contain plugin projects. Contains two plugin projects
  * `com.polarion.tycho.build.service` that provides a velocity context key `$myService` accessible from Polarion classic wiki and rich pages and
  * `com.polarion.tycho.build.web` that uses the same service to generate an output accessible from http://[polarion_host]/polarion/polariontychotest.
* `features` that contains feature projects that aggregate a set of plugins. Contains a single project `com.polarion.tycho.build.helloworldsample` that contains all plugins of this project.
* `releng` that contains
  * `target-platform`, the previously build update site as target definition using http://localhost:8080/repository and
  * `update-site`, which will contain the plugins and features of this project on successful build.

## Notes on Tycho POM-less feature
The use of Tycho POM-less feature provides the benefit that for the different Tycho [packaging types](https://wiki.eclipse.org/Tycho/Packaging_Types), a dedicated pom.xml is not required but is automatically derived from existing configurations that emerge during plugin development (MANIFEST.MF, build.properties, feature.xml, ...). If a plugin has special requirements where the use of a dedicated pom.xml, e.g. to define additional build plugins, a dedicated pom.xml can be defined for that plugin. See [this](http://blog.vogella.com/2019/11/25/pom-less-tycho-enhanced/) blog post that demonstrates how. If you only need to specify maven properties, then you can do so without a pom by adding  `pom.model.property.<property>=<value>` to the `build.properties` file (see [Tycho Release Note 2.0](https://wiki.eclipse.org/Tycho/Release_Notes/2.0#Define_Maven_Project_properties_in_build.properties)). For example, when using maven-based SonarQube integration, the use of special sonar properties need to be specified in pom as maven properties. Specifying `pom.model.property.sonar.sources=src,webapp` in the `build.properties` will be equivalent to
```xml
<properties>
    <sonar.sources>src,webapp</sonar.sources>
</properties>
```
in the pom file.
