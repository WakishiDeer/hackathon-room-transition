const request = require('request');

let KINTONE_ID=2
let KINTONE_APP=5

let params = {
  url: 'https://yrx1kimhweye.cybozu.com/k/v1/record.json?app=100&id=1',
  method: 'PUT',
  json: true,
  form:{
    "app":KINTONE_APP,
    "id":KINTONE_ID,
    "record":{
      "employee_id":{
        "value":data
      }
    }
  },
  headers: {
    'X-Cybozu-API-Token': 'OXZWieroA888rUkNVPswfWxWGpg1D1hmb1ZR84jq',
  },
};

request(params, function(err, resp, body) {
  if (err) {
    console.log(err);
    return;
  }
  console.log(body);
});
