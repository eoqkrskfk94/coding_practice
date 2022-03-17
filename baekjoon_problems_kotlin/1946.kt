import kotlin.math.max

fun main(args: Array<String>) {
    val br = System.`in`.bufferedReader()

    val testCount = br.readLine().toInt()
    val answers = mutableListOf<Int>()

    for(i in 0 until testCount) {
        val peopleCount = br.readLine().toInt()
        val grades = mutableListOf<List<Int>>()
        for(j in 0 until peopleCount) {
            val grade = br.readLine().split(" ").map { it.toInt() }
            grades.add(grade)
        }
        grades.sortWith(compareBy { it[0] })
        answers.add(getRecruitmentNumber(grades))
    }

    answers.forEach { println(it) }
}

fun getRecruitmentNumber(grades: MutableList<List<Int>>): Int {

    var recruitmentNumber = 1
    var threshold = grades[0][1]

    for(i in 1 until grades.size) {
        if(grades[i][1] <= threshold){
            recruitmentNumber++
            threshold = grades[i][1]
        }
    }

    return recruitmentNumber
}




