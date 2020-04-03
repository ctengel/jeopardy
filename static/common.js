
function time2read(timemili) {
	var disptime = new Date(timemili);
	return disptime.getHours().toString().padStart(2, '0') + ':' + disptime.getMinutes().toString().padStart(2, '0') + ':' + disptime.getSeconds().toString().padStart(2, '0') + '.' + disptime.getMilliseconds().toString().padStart(3, '0');
}

function processbuzz(x) {
	var node = document.createElement('li');
	var textnode = document.createTextNode(time2read(x['datetime']) + ' - ' + x['person']);
	node.appendChild(textnode);
	document.getElementById('buzzes').appendChild(node);
	return x['datetime'];
}
