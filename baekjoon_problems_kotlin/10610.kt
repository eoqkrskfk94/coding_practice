fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var number = br.readLine().toList().map { it.digitToInt() }


    number = number.sorted().reversed()

    if(checkIfNotDividableBy(number)) {
        println("-1")
    } else {
        if(number.sum() % 3 != 0) {
            println("-1")
        } else {
            println(number.joinToString(""))
        }
    }
}

fun checkIfNotDividableBy(numberList: List<Int>): Boolean {
    return !numberList.contains(0)
}

