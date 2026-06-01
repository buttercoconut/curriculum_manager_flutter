class Grade {
  final int id;
  final String name;
  final String className;
  final int studentCount;

  Grade({
    required this.id,
    required this.name,
    required this.className,
    required this.studentCount,
  });

  factory Grade.fromJson(Map<String, dynamic> json) {
    return Grade(
      id: json['id'],
      name: json['name'],
      className: json['class_name'],
      studentCount: json['student_count'],
    );
  }
}
