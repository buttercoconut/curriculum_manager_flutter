import 'package:flutter/material.dart';

class GradeCard extends StatelessWidget {
  final String subject;
  final double score;

  const GradeCard({Key? key, required this.subject, required this.score}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.all(8.0),
      child: ListTile(
        leading: const Icon(Icons.grade),
        title: Text(subject),
        trailing: Text(score.toStringAsFixed(1)),
      ),
    );
  }
}
