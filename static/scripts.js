function get(){
 const url = 'http://127.0.0.1:8000/get';
 const query1 = 'url='+document.getElementById('geturl').value;
// const query2 = 'param2=value2';
const queryString = [query1].filter(q => q).join('&');
fetch(`${url}?${queryString}`, {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  },
//   body: JSON.stringify(requestBody)
})
  .then(response => response.json())
  .then(data => {
    document.getElementById('time').innerHTML = JSON.stringify(data.time);
    document.getElementById('code').innerHTML = JSON.stringify(data.status_code);
    document.getElementById('size').innerHTML = JSON.stringify(data.size);
    document.getElementById('headers').innerHTML = `<pre>${JSON.stringify(data.headers,null,2)}</pre>`
    document.getElementById('body').innerHTML = `<pre>${JSON.stringify(data.body,null,2)}</pre>`
    const len = Object.keys(data.headers).length
    document.getElementById('len').innerHTML=JSON.stringify(len)
  })
  .catch(error => console.error(error));
}

function post(){
  const url = 'http://127.0.0.1:8000';
  const queryParams = new URLSearchParams({
  url: document.getElementById('posturl').value,
  request_body: document.getElementById('post_req_body').value
  });

  fetch(`${url}/post?${queryParams}`, {
    method: 'POST'
  })
  .then(response => response.json())
  .then(data => {
  document.getElementById('time').innerHTML=JSON.stringify(data.time)
  document.getElementById('code').innerHTML = JSON.stringify(data.status_code);
  document.getElementById('size').innerHTML = JSON.stringify(data.size);
  document.getElementById('headers').innerHTML = `<pre>${JSON.stringify(data.headers,null,1)}<pre>`;
  document.getElementById('body').innerHTML = `<pre>${JSON.stringify(data.body,null,1)}</pre>`;
  const len = Object.keys(data.headers).length
  document.getElementById('len').innerHTML=JSON.stringify(len)
  })
  .catch(error => console.error(error))
}

function put(){
  const url = 'http://127.0.0.1:8000';
  const queryParams = new URLSearchParams({
  url: document.getElementById('puturl').value,
  body: document.getElementById('put_req_body').value
  });

  fetch(`${url}/put?${queryParams}`, {
    method: 'PUT'
  })
  .then(response => response.json())
  .then(data => {
  document.getElementById('time').innerHTML=JSON.stringify(data.time);
  document.getElementById('code').innerHTML = JSON.stringify(data.status_code);
  document.getElementById('size').innerHTML = JSON.stringify(data.size);
  document.getElementById('headers').innerHTML = `<pre>${JSON.stringify(data.headers)}</pre>`;
  document.getElementById('body').innerHTML = `<pre>${JSON.stringify(data.body)}</pre>`;
  const len = Object.keys(data.headers).length;
  document.getElementById('len').innerHTML=JSON.stringify(len);
  })
  .catch(error => console.error(error))
}

function del(){
    const url = 'http://127.0.0.1:8000';
    const queryParams = new URLSearchParams({
    url: document.getElementById('deleteurl').value,
    });
    fetch(`${url}/delete?${queryParams}`, {
      method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
    document.getElementById('time').innerHTML=JSON.stringify(data.time)
    document.getElementById('code').innerHTML = JSON.stringify(data.status_code);
    document.getElementById('size').innerHTML = JSON.stringify(data.size);
    document.getElementById('headers').innerHTML = `<pre>${JSON.stringify(data.headers)}</pre>`;
    document.getElementById('body').innerHTML = `<pre>${JSON.stringify(data.body)}</pre>`;
    const len = Object.keys(data.headers).length;
    document.getElementById('len').innerHTML=JSON.stringify(len);
    })
    .catch(error => console.error(error))
}
