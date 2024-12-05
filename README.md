# polarion-tycho-example
Demonstrates how Eclipse Tycho can be setup to build Polarion ALM plugins using Tycho POM-less feature.

## Required software
* Polarion ALM (2410 was used)
* JDK as required by your Polarion installation (17 in this demo)
* Python 3

Maven wrappers have been provided to enable build execution without the user requiring a maven installation.

## How to build the example
* Ensure that the `<location>` element in `releng/target-platform/target-platform.xml` points to your Polarion plugins path. 
* Execute `mvnw clean verify` (Windows) or `./mvnw clean verify` (Linux) to run the build.
* On build success, the plugins will be available at `releng/update-site/repo-to-runnable`.

## Project overview
The project is structured as follows:
* `bundles` that will contain your plugin projects. Currently contains two plugin projects
    * `com.polarion.tycho.build.service` that provides a velocity context key `$myService` accessible from Polarion classic wiki and rich pages and
    * `com.polarion.tycho.build.web` that uses the same service to generate an output accessible from http://[polarion_host]/polarion/polariontychotest.
* `features` that contains feature projects for aggregating a set of plugins. The example contains a single project `com.polarion.tycho.build.helloworldsample` containing above plugins.
* `releng` that contains
    * `target-platform` where you specify the Polarion platform or any additional target platform dependencies and
    * `update-site` that references the feature and will contain the plugins on successful build.

## Notes on Tycho POM-less feature
This project has been enabled for POM-less development, meaning that for the different [tycho packaging types](https://wiki.eclipse.org/Tycho/Packaging_Types) (bundles, features, update-site etc.),
you do not need to specify a dedicated `pom.xml`.  If you have special build requirements like additional maven build plugins, a `pom.xml` may be specified (example: `releng/update-site/pom.xml`).

If you only need to specify maven properties, then you can do so without a pom by adding  `pom.model.property.<property>=<value>` to the `build.properties` file
(see [Define Properties](https://github.com/eclipse-tycho/tycho/wiki/Tycho-Pomless#define-properties)).
For example, when using maven-based SonarQube integration, you may need to specify which source folders SonarQube should scan.
Specifying `pom.model.property.sonar.sources=src,webapp` in the `build.properties` will then be equivalent to
```xml
<properties>
    <sonar.sources>src,webapp</sonar.sources>
</properties>
```
in the pom file.

## Resources
[GitHub - eclipse-tycho/tycho](https://github.com/eclipse-tycho/tycho)
[Karlsruher Institut für Technologie - Maven Tycho](https://sdqweb.ipd.kit.edu/wiki/Maven_Tycho)  
[Eclipse Tycho Release Notes](https://wiki.eclipse.org/Tycho/Release_Notes)  
[Eclipse Tycho Release Notes (2.4 and newer)](https://github.com/eclipse/tycho/blob/master/RELEASE_NOTES.md)  
[Vogella Eclipse Tycho Tutorial](https://www.vogella.com/tutorials/EclipseTycho/article.html)  
[Tycho/pomless](https://wiki.eclipse.org/Tycho/pomless)  
[POM-less Tycho enhanced](http://blog.vogella.com/2019/11/25/pom-less-tycho-enhanced/)
