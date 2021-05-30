const request = require('request');

let params = {
  url: 'https://yrx1kimhweye.cybozu.com/k/v1/record.json?app=100&id=1',
  method: 'GET',
  json: true,
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
