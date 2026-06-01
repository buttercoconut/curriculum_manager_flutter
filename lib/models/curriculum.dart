class Curriculum {
  final int id;
  final String title;
  final String description;
  final int gradeLevel;
  final List<String> subjects;

  Curriculum({
    required this.id,
    required this.title,
    required this.description,
    required this.gradeLevel,
    required this.subjects,
  });

  factory Curriculum.fromJson(Map<String, dynamic> json) {
    return Curriculum(
      id: json['id'],
      title: json['title'],
      description: json['description'],
      gradeLevel: json['grade_level'],
      subjects: List<String>.from(json['subjects'] ?? []),
    );
  }
}
