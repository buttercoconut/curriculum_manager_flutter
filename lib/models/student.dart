class Student {
  final int id;
  final String name;
  final int gradeLevel;
  final String className;

  Student({
    required this.id,
    required this.name,
    required this.gradeLevel,
    required this.className,
  });

  factory Student.fromJson(Map<String, dynamic> json) {
    return Student(
      id: json['id'],
      name: json['name'],
      gradeLevel: json['grade_level'],
      className: json['class_name'],
    );
  }
}
