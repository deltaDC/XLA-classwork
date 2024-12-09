import re

def extract_dependency_name(jar_name):
    """Extract the dependency name without version from the JAR name."""
    match = re.match(r"(.+?)-\d", jar_name)
    return match.group(1) if match else jar_name

def parse_jar_versions(jar_list):
    """Create a mapping of dependency name to its version from a list of JARs."""
    version_map = {}
    for jar in jar_list:
        dependency_name = extract_dependency_name(jar)
        version = jar[len(dependency_name) + 1:].replace(".jar", "")  # Extract version
        version_map[dependency_name] = version
    return version_map

def get_input_list():
    """Collect a list of JAR file names from the user."""
    input_list = []
    while True:
        user_input = input()
        if user_input == "0":
            break
        else:
            input_list.append(user_input)
    return input_list

def main():
    print("Enter JAR file names (type '0' to stop):")
    jar_list_1 = get_input_list()

    print("\nEnter second list of JAR file names (type '0' to stop):")
    jar_list_2 = get_input_list()

    # Parse JAR dependencies and versions
    version_map_1 = parse_jar_versions(jar_list_1)
    version_map_2 = parse_jar_versions(jar_list_2)

    # Unique dependencies in list 1 but not in list 2
    unique_to_list_1 = set(version_map_1.keys()) - set(version_map_2.keys())

    # Dependencies with differing versions
    diff_version_list = []
    for dependency in version_map_1.keys() & version_map_2.keys():
        if version_map_1[dependency] != version_map_2[dependency]:
            diff_version_list.append(f"{dependency}: {version_map_1[dependency]} -> {version_map_2[dependency]}")

    # Print results
    print("\nDependencies in the first list but not in the second list:")
    if unique_to_list_1:
        for dependency in unique_to_list_1:
            print(dependency)
    else:
        print("No dependencies are unique to the first list.")

    print("\nDependencies with differing versions:")
    if diff_version_list:
        for diff in diff_version_list:
            print(diff)
    else:
        print("No dependencies have differing versions.")

if __name__ == "__main__":
    main()


# new dependencies list
# accessors-smart-1.1.jar
# android-json-0.0.20131108.vaadin1.jar
# antlr-2.7.7.jar
# asm-5.0.3.jar
# aspectjweaver-1.8.14.jar
# assertj-core-2.6.0.jar
# classmate-1.3.4.jar
# dom4j-1.6.1.jar
# hamcrest-core-1.3.jar
# hamcrest-library-1.3.jar
# hibernate-commons-annotations-5.0.1.Final.jar
# hibernate-core-5.0.12.Final.jar
# hibernate-entitymanager-5.0.12.Final.jar
# hibernate-jpa-2.1-api-1.0.0.Final.jar
# hibernate-validator-5.3.6.Final.jar
# jackson-annotations-2.8.0.jar
# jackson-core-2.8.11.jar
# jackson-databind-2.8.11.3.jar
# jandex-2.0.0.Final.jar
# javassist-3.21.0-GA.jar
# javax.transaction-api-1.2.jar
# jboss-logging-3.3.2.Final.jar
# jcl-over-slf4j-1.7.26.jar
# json-path-2.2.0.jar
# json-smart-2.2.1.jar
# jsonassert-1.4.0.jar
# jul-to-slf4j-1.7.26.jar
# junit-4.12.jar
# log4j-over-slf4j-1.7.26.jar
# logback-classic-1.1.11.jar
# logback-core-1.1.11.jar
# mockito-core-1.10.19.jar
# objenesis-2.1.jar
# slf4j-api-1.7.26.jar
# snakeyaml-1.17.jar
# spring-aop-4.3.25.RELEASE.jar
# spring-aspects-4.3.25.RELEASE.jar
# spring-beans-4.3.25.RELEASE.jar
# spring-boot-1.5.22.RELEASE.jar
# spring-boot-autoconfigure-1.5.22.RELEASE.jar
# spring-boot-starter-1.5.22.RELEASE.jar
# spring-boot-starter-aop-1.5.22.RELEASE.jar
# spring-boot-starter-data-jpa-1.5.22.RELEASE.jar
# spring-boot-starter-jdbc-1.5.22.RELEASE.jar
# spring-boot-starter-logging-1.5.22.RELEASE.jar
# spring-boot-starter-test-1.5.22.RELEASE.jar
# spring-boot-starter-tomcat-1.5.22.RELEASE.jar
# spring-boot-starter-web-1.5.22.RELEASE.jar
# spring-boot-starter-websocket-1.5.22.RELEASE.jar
# spring-boot-test-1.5.22.RELEASE.jar
# spring-boot-test-autoconfigure-1.5.22.RELEASE.jar
# spring-context-4.3.25.RELEASE.jar
# spring-core-4.3.25.RELEASE.jar
# spring-data-commons-1.13.23.RELEASE.jar
# spring-data-jpa-1.11.23.RELEASE.jar
# spring-expression-4.3.25.RELEASE.jar
# spring-jdbc-4.3.25.RELEASE.jar
# spring-messaging-4.3.25.RELEASE.jar
# spring-orm-4.3.25.RELEASE.jar
# spring-test-4.3.25.RELEASE.jar
# spring-tx-4.3.25.RELEASE.jar
# spring-web-4.3.25.RELEASE.jar
# spring-webmvc-4.3.25.RELEASE.jar
# spring-websocket-4.3.25.RELEASE.jar
# tomcat-annotations-api-8.5.43.jar
# tomcat-embed-core-8.5.43.jar
# tomcat-embed-el-8.5.43.jar
# tomcat-embed-websocket-8.5.43.jar
# tomcat-jdbc-8.5.43.jar
# tomcat-juli-8.5.43.jar
# validation-api-1.1.0.Final.jar



# old dependencies list
# antlr-2.7.6.jar
# aopalliance.jar
# api-common-1.0.0-rc1.jar
# aspectjrt.jar
# aspectjweaver-1.6.8.jar
# auto-value-1.1.jar
# bcrypt-0.9.0-javadoc.jar
# bcrypt-0.9.0.jar
# bytes-1.3.0.jar
# c3p0-0.9.1.2.jar
# cglib-nodep-3.1.jar
# com.ibm.icu_3.4.4.1.jar
# commons-collections-3.1.jar
# commons-dbcp-1.4.jar
# commons-fileupload-1.2.1.jar
# commons-io-1.3.1.jar
# commons-lang.jar
# commons-logging-1.1.jar
# commons-pool-1.5.5.jar
# dom4j-1.6.1.jar
# error_prone_annotations-2.0.19.jar
# grpc-context-1.7.0.jar
# grpc-core-1.7.0.jar
# grpc-netty-1.7.0.jar
# grpc-protobuf-1.7.0.jar
# grpc-protobuf-lite-1.7.0.jar
# grpc-stub-1.7.0.jar
# gson-2.7.jar
# guava-19.0.jar
# gwt-charts-0.9.8.jar
# gwt-maps-javadoc.jar
# gwt-maps.jar
# gwt-servlet-deps.jar
# gwt-servlet.jar
# gwt-user-1.4.62.jar
# gwteventservice-1.0.2.jar
# gxt-2.2.4-gwt22.jar
# gxt-2.2.5-gwt22.jar
# hibernate-jpa-2.0-api-1.0.1.Final.jar
# hibernate-validator-4.2.0.Final.jar
# hibernate3.jar
# httpclient-4.5.6.jar
# httpclient-cache-4.5.6.jar
# httpclient-win-4.5.6.jar
# httpcore-4.4.4.jar
# imap-1.6.0.jar
# instrumentation-api-0.4.3.jar
# iomail.jar
# iText-2.1.2u.jar
# itextpdf-5.5.13.jar
# jackson-all-1.9.9.jar
# jackson-annotations-2.6.6.jar
# jackson-core-2.1.4.jar
# jackson-core-asl-1.9.13.jar
# jackson-databind-2.1.4.jar
# jackson-mapper-asl-1.9.13.jar
# javassist-3.12.0.GA.jar
# javax.mail.jar
# joda-time-2.8.2.jar
# jsr305-3.0.0.jar
# jta-1.1.jar
# jtds-1.2.5.jar
# junit-4.4.jar
# kernel-7.0.0.jar
# log4j-1.2.16.jar
# mailapi-1.6.3.jar
# netty-buffer-4.1.16.Final.jar
# netty-codec-4.1.16.Final.jar
# netty-codec-http-4.1.16.Final.jar
# netty-codec-http2-4.1.16.Final.jar
# netty-codec-socks-4.1.16.Final.jar
# netty-common-4.1.16.Final.jar
# netty-handler-4.1.16.Final.jar
# netty-handler-proxy-4.1.16.Final.jar
# netty-resolver-4.1.16.Final.jar
# netty-transport-4.1.16.Final.jar
# ojdbc8.jar
# okhttp-3.9.0.jar
# okio-1.13.0.jar
# opencensus-api-0.6.0.jar
# poi-3.5-FINAL.jar
# poi-3.7-20101029.jar
# poi-3.9-20121203.jar
# poi-examples-3.7-20101029.jar
# poi-ooxml-3.7-20101029.jar
# poi-ooxml-3.9-20121203.jar
# poi-ooxml-schemas-3.7-20101029.jar
# poi-ooxml-schemas-3.9-20121203.jar
# poi-scratchpad-3.7-20101029.jar
# poi-scratchpad-3.9-20121203.jar
# pop3.jar
# proto-google-common-protos-0.1.9.jar
# protobuf-java-3.4.0.jar
# protobuf-java-util-3.4.0.jar
# servlet-api-2.5.jar
# slf4j-api-1.6.1.jar
# slf4j-log4j12-1.6.4.jar
# smtp.jar
# spring-aop-4.3.25.RELEASE.jar
# spring-aspects-4.3.25.RELEASE.jar
# spring-beans-4.3.25.RELEASE.jar
# spring-context-4.3.25.RELEASE.jar
# spring-context-support-4.3.25.RELEASE.jar
# spring-core-4.3.25.RELEASE.jar
# spring-expression-4.3.25.RELEASE.jar
# spring-instrument-4.3.25.RELEASE.jar
# spring-instrument-tomcat-4.3.25.RELEASE.jar
# spring-jdbc-4.3.25.RELEASE.jar
# spring-jms-4.3.25.RELEASE.jar
# spring-messaging-4.3.25.RELEASE.jar
# spring-orm-4.3.25.RELEASE.jar
# spring-oxm-4.3.25.RELEASE.jar
# spring-test-4.3.25.RELEASE.jar
# spring-tx-4.3.25.RELEASE.jar
# spring-web-4.3.25.RELEASE.jar
# spring-webmvc-4.3.25.RELEASE.jar
# spring-webmvc-portlet-4.3.25.RELEASE.jar
# spring-websocket-4.3.25.RELEASE.jar
# spring4gwt-0.0.1.jar
# tensorflow-serving-connector.jar
# validation-api-1.0.0.GA-sources.jar
# validation-api-1.0.0.GA.jar
# xmlbeans-2.6.0.jar


# Dependencies in the first list but not in the second list:
# snakeyaml
# spring-boot-starter-data-jpa
# classmate
# spring-boot-starter-websocket
# spring-boot-starter-logging
# javax.transaction-api
# spring-boot-test
# android-json
# jcl-over-slf4j
# hibernate-core
# spring-data-jpa
# spring-boot
# hamcrest-library
# jandex
# accessors-smart
# spring-boot-starter
# logback-core
# mockito-core
# spring-boot-test-autoconfigure
# hibernate-commons-annotations
# json-smart
# spring-boot-starter-web
# logback-classic
# spring-boot-autoconfigure
# hamcrest-core
# jsonassert
# tomcat-embed-el
# assertj-core
# spring-boot-starter-aop
# log4j-over-slf4j
# tomcat-embed-websocket
# spring-boot-starter-tomcat
# objenesis
# spring-boot-starter-jdbc
# spring-boot-starter-test
# tomcat-annotations-api
# json-path
# asm
# tomcat-juli
# jul-to-slf4j
# hibernate-entitymanager
# tomcat-embed-core
# tomcat-jdbc
# jboss-logging
# spring-data-commons
#
# Dependencies with differing versions:
# hibernate-jpa: 2.1-api-1.0.0.Final -> 2.0-api-1.0.1.Final ok
# slf4j-api: 1.7.26 -> 1.6.1 ok
# validation-api: 1.1.0.Final -> 1.0.0.GA ok
# antlr: 2.7.7 -> 2.7.6 ok
# junit: 4.12 -> 4.4 ok
# javassist: 3.21.0-GA -> 3.12.0.GA ok
# jackson-annotations: 2.8.0 -> 2.6.6 ok
# jackson-databind: 2.8.11.3 -> 2.1.4 ok
# jackson-core: 2.8.11 -> 2.1.4 ok
# aspectjweaver: 1.8.14 -> 1.6.8 ok
# hibernate-validator: 5.3.6.Final -> 4.2.0.Final


# filtered dependencies list to copy from first list to second list
# snakeyaml ok
# classmate ok
# javax.transaction-api ok
# android-json ok
# jcl-over-slf4j ok
# hamcrest-library ok
# jandex ok
# accessors-smart ok
# logback-core ok
# json-smart ok
# logback-classic ok
# hamcrest-core ok
# jsonassert ok
# assertj-core  ok
# log4j-over-slf4j ok
# objenesis ok
# json-path ok
# asm ok
# jul-to-slf4j ok
# jboss-logging ok
