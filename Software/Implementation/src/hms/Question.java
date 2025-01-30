
package src.hms;

public class Question {
    private String questionText;
    private String answer;

    private Patient patient;
    private Doctor doctor;

    public String getQuestionText() {
        return questionText; // Return question text
    }

    public void setQuestionText(String questionText) {
        this.questionText = questionText; // Set question text
    }

    public String getAnswer() {
        return answer; // Return answer
    }

    public void setAnswer(String answer) {
        this.answer = answer; // Set answer
    }
}
