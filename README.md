Description

The scope of this portion of the project is to create a data generation script that conforms to the Wisconsin Benchmark, create a database instance, define a schema based on the Wisconsin Benchmark format, and upload the data to the newly created database.

System

This database is hosted on a MySQL MariaDB 10.0 instance on a cloud backend.  This cloud backend is a corporate system that is not publicly accessible. To interface with this system, I am using MySQL Workbench, which is a Windows based SQL management GUI.

Generating Data

Generating the data specified in the Wisconsin Benchmark paper is done with a Python 2.7 script. This data is printed in a CSV format to a file. The first row is are the attribute names, followed by data that meets the standards for the paper. For the purpose of this project portion, a tuple size of 1000 is used. 
The convert function from the Wisconsin Benchmark is adapted for this script in a Python format. The code may be viewed for further specific details.

Loading Data

The data is uploaded using Workbench. The CSV and be directly uploaded using the CSV import tool. This function is also configured to ignore primary key duplicate errors. Due to duplicate primary keys, 650 total entries were able to be uploaded to the database. This same method is followed for each table creation. 
Lessons

There are two major lessons to be learned from this implementation. First, adapting the sample code was difficult and took multiple iterations due to the source changing. The paper did not specify what the ideal case should be, but only insisted the example code should be used. The issue was that the example code was not bug free, and it was difficult to determine what the exact output should be.
Secondly, 1000 tuples for an upload takes over twenty minutes with my current method. A better implementation would be to write a SQL script that uses server-side procedures to generate and insert the data. This would eliminate the need for a lengthy upload, and would be useful for tuple counts of larger magnitude. 
