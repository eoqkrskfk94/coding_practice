fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    val changes = listOf(500, 100, 50, 10, 5, 1)
    val payment = br.readLine().toInt()
    var change = 1000 - payment
    var changeCount = 0

    changes.forEach {
        if(change / it > 0) {
            changeCount += change / it
            change %= it
        }
    }

    println(changeCount)


}



