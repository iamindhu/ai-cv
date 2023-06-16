var Minio = require('minio');
// console.log("1");
// Instantiate the minio client with the endpoint
// and access keys as shown below.
var minioClient = new Minio.Client({
    endPoint: '127.0.0.1',
    port: 9000,
    useSSL: false,
    accessKey: 'dnyEzXvlcu1jzcy9viOt',
    secretKey: 'utCBA7Pi0F6LLjD13FT9hve0qO22Uhpb48mIi591'
});
// console.log("1");

// File that needs to be uploaded.http://127.0.0.1:9090/browser/uploads
var file = 'reducer.py';
// console.log("1");

// Make a bucket called europetrip.
// minioClient.makeBucket('CompUpload', 'us-east-1', function(err) {
//     if (err) return console.log(err)

//     console.log('Bucket created successfully in "us-east-1".')
// console.log("1");

var metaData = {
    'Content-Type': 'application/octet-stream',
    'X-Amz-Meta-Testing': 1234,
    'example': 5678
};
// Using fPutObject API upload your file to the bucket europetrip.
// console.log("1");

minioClient.fPutObject('uploads', 'reducer.py', file, metaData, function(err, etag) {
    if (err) return console.log(err)
    console.log('File uploaded successfully.')
});
// });
