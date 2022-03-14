fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var numOfRopes = br.readLine().toInt()
    var ropes = mutableListOf<Int>()
    var totalWeight = 0
    var totalRopes = 0



    repeat(numOfRopes) {
        val rope = br.readLine().toInt()
        ropes.add(rope)

    }

    ropes = ropes.sorted().reversed().toMutableList()

    for (i in 0 until ropes.size) {
        if(ropes[i] * (i+1) > totalWeight) {
            totalWeight = ropes[i] * (i+1)
        }
    }


    println(totalWeight)

}