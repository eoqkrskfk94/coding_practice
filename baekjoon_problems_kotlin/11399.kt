fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    var numOfPeople = br.readLine().toInt()

    val timeTakenArray = br.readLine().split(" ").map { it.toInt() }.sorted().toTypedArray()



    var timeTaken = 0
    var total = 0

    timeTakenArray.forEach {
        timeTaken += it
        total += timeTaken
    }

    println(total)

}