function formatDate(date) {
    var d = new Date()
    return d.toISOString().split('T')[0]
}

