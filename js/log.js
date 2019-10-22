
function log () {

	Array.from(arguments).forEach(arg => {
		var p = document.createElement('p')
		p.innerHTML = arg
		cons.appendChild(p)
	})
}
