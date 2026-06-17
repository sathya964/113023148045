GET/api/notifications
Response
{
    "notifications":[
        {
            "id":"1",
            "message":"Placement Drive",
            "type":"Placement",
            "isRead":false,
            "createdAt":"2026-04-22T17:51:18"
        }
    ]
}
PUT/api/notifications/{id}/read
Response
{
    "message":"Notification marked as read"
}
POST/api/notifications
Request
{
    "message":"Placement Drive",
    "type":"Placement"
}
Response
{
    "message":"Notification created"
}


postgreSQL
-ACID compliance
-Reliable transactions
-Good indexing support
-Scalable
Students Table
studentID BIGINT PRIMARY KEY
name VARCHAR(100)
Notifications Table
id UUID PRIMARY KEY
studentID BIGINT
message TEXT
notificationType VARCHAR(20)
isRead BOOLEAN
createdAt TIMESTAMP
-Slow queries
-Large table scans
-Indexing
-Catching
-Pagination
-Partitioning
SELECT*
FROM notifications
WHERE studentID=1042;


The query is correct but slow because the table contains millions of rows
original Query
SELECT*
FROM notifications
WHERE studentID=1042
AND isRead=false
ORDER BY createdAt ASC;

Reason
-Full table scan
-no index
Solution
CREATE INDEX idx_notifications_student_read
ON notifications(studentID,isRead,createdAt);
Optimized Query
SELEECT*
FROM notifications
WHERE studentID=1042
AND isRead=false
ORDER BY createdAt ASC;

cost
O(log N)
Adding indexes on every column is not recommended because:
-more storage
-slower inserts
-higher maintainance cost

Placement Query
SELECT*
FROM notifications
WHERE notificationType="Placement"
AND createdAt>=NOW()-INTERVAL'7 days';

Problem
Database is queried on every page load.
Solutions
1.Redis Cache
Advantages
-Faster response
Disadvantages
-Extra memory
2.Pagination
Advantages
-Smaller result sets
Disadvantages
-Multiple requests
3.WebSockets
Advantages
-Real-time updates
Disadvantages
-More server connections

Problems
-Sequential processing
-Slow for 50000 students
-Email failures cause inconsistancy
Solution
Use Queue System
HR
-Queue
-Workers
email services
-notificsgtion service
-
Benifits
-Retry support
Fault toleatnce 
-Fast exectuion

Approach
Use priority Quese (Heap)
priorty
Placement=3
Result=2
event=1
O(log n)

Frontend
React + Material UI
pages
1.ALL Notifications
Features
-Pagination
-Filtering
-Mark as Read
2.Priority Notifications
Features
-top N Notifications
-Filter by type
Logging Middleware
Integrated for all API calls
Responsive Design
-Desktop
-Mobile
Error Handling
-API Failure
-Empty Response
-Invalid Data