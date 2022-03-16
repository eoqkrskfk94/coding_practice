fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var equations = br.readLine().toString().split("-")

    val addNumbers = equations[0].split("+").sumOf { it.toInt() }

    var minusNumbers = 0

    for (i in 1 until equations.size) {
        minusNumbers -= equations[i].split("+").sumOf { it.toInt() }
    }

    println(addNumbers + minusNumbers)


}



