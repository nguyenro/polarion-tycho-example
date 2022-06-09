# polarion-target-platform

This project helps to accomplish the following:
* Create a p2 update site containing Polarion plugins
* Serve the update site locally at http://localhost:8080/repository so that the Polarion target platform can be consumed as software site.

## Steps to create a p2 update site
* In eclipse, open the file `releng/target-platform/target-platform.target` of this project and ensure that in the `Definition` tab, the location points to the plugins folder of your Polarion installation. The location is set to `C:\Polarion\polarion` by default.
* In the `Content` tab, unselect all linux fragments.
  * org.eclipse.core.filesystem.linux.x86_64
  * org.eclipse.core.net.linux.x86_64
  * org.eclipse.equinox.launcher.gtk.linux.x86_64
  * org.eclipse.equinox.security.linux.x86_64
* Save the changes.
* Change the target platform through the eclipse menu `Window > Preferences > Plug-in Development > Target Platform` and select the `target-platform` file corresponding to this project and apply the selection.
* Open the file `features/com.polarion.platform.api/feature.xml` of this project and in the `Included Plug-ins` tab, add all plugins belonging to the Polarion target platform. Note: Take care to only select the plugins provided by Polarion as plugins from your workspace appears in the selection as well. A helpful indicator is to check the total count of plugins displayed here and the plugin count displayed in `releng/target-platform/target-platform.target` match.
* Save the changes.
* Open a terminal at the root of this project where the pom.xml and pom.jetty.xml is located, then execute `mvnw clean verify` (Windows) or `./mvnw clean verify` (Linux).
* On successful build, the p2 update site will be available at `releng/update-site/target/repository`.
* In the same terminal, execute `mvnw -f pom.jetty.xml jetty:run` or `./mvnw -f pom.jetty.xml jetty:run` that will serve the update site at http://localhost:8080/repository. Close the terminal or press `Ctrl + C` to stop serving the update site.

The update site can be hosted on a web server that is accessible from your continuous integration system to enable Tycho to resolve Polarion plugins against it during the build stage. From here on, you can continue with the `polarion-tycho-build/README.me`.
