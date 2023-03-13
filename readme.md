Implementation on a chosen ORM, Django, of a database that defines a dynamic permission system. The required implementation concerns only a graphical representation of the designed architecture and the definition of the models at the code level using the chosen ORM. The time to perform the task is 1 week.
The system should allow the assignment of Groups or Permissions to generic users. There will be a system group that cannot be modified, called "SuperAdmin" which will have all platform permissions.
 
A group is represented by the following fields:
- group name
- permissions associated with the group
- users belonging to the group

A user can be assigned one or more groups, and one or more specific permissions can also be assigned. Therefore, individual permissions assigned to users take precedence over those of the groups.

A user with sufficient permissions can create a custom group. In this group, the user creating it can assign permissions related to the permissions currently available to the user, and equal to or lower in degree among the available permissions.

A permission is represented by the following fields:
- name
- type of permission (create, edit, delete, view)
- associated specific resource (optional), if null then it is a class permission
- degree, which is an inversely ordered number indicating the hierarchy among permissions. The larger it is, the more it concerns specific resources, the smaller it is, the more it concerns general resources.

Permissions can be of two types:
- Class permissions are pre-existing in the platform and therefore concern all entities present in the platform itself.
Instance permissions, on the other hand, are created automatically at the creation of any resource that requires a permission (so everything), and therefore represent the ability to perform one of the 4 possible actions, already described above, on the specific resource.
- Users will be able to assign one or more groups, both system and custom, and in addition to the groups, specific permissions can also be assigned. Based on the groups and permissions assigned to the user, they will be able to perform certain actions.

What we will want to see are:
- the definitions of the models on code;
- a graphical representation of the entire database;
- DRF based REST APIs to manipulate this data.
