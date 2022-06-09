# polarion-tycho-example
Demonstrates how Eclipse Tycho can be setup to build Polarion ALM plugins using Tycho POM-less feature.

## Required software
* Eclipse IDE (RCP and RAP Developers 2021-12 was used)
* JDK 11
* Polarion ALM (21 R1 was used)

Maven wrapper have been provided to enable build execution without the user requiring a maven installation.

## How to use
This repository contains two eclipse projects at its root:
* `polarion-target-platform` to aid creation of Polarion plugins as p2 update site.
* `polarion-tycho-build` containing a simple project which is built against the Polarion update site as target platform.

Import those projecs into eclipse, including their nested projects.

To get the build working, follow the steps described in `polarion-target-platform/README.md`, then proceed with `polarion-tycho-build/README.md`.

## Resources
[Karlsruher Institut für Technologie - Maven Tycho](https://sdqweb.ipd.kit.edu/wiki/Maven_Tycho)  
[Eclipse Tycho Release Notes](https://wiki.eclipse.org/Tycho/Release_Notes)  
[Eclipse Tycho Release Notes (2.4 and newer)](https://github.com/eclipse/tycho/blob/master/RELEASE_NOTES.md)  
[Vogella Eclipse Tycho Tutorial](https://www.vogella.com/tutorials/EclipseTycho/article.html)  
[Tycho/pomless](https://wiki.eclipse.org/Tycho/pomless)  
[POM-less Tycho enhanced](http://blog.vogella.com/2019/11/25/pom-less-tycho-enhanced/)