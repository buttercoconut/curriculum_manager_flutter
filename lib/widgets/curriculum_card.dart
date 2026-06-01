import 'package:flutter/material.dart';
import '../models/curriculum.dart';

class CurriculumCard extends StatelessWidget {
  final Curriculum curriculum;

  const CurriculumCard({Key? key, required this.curriculum}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
      child: ListTile(
        title: Text(curriculum.title, style: const TextStyle(fontWeight: FontWeight.bold)),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 4),
            Text(curriculum.description),
            const SizedBox(height: 4),
            Text('Grade Level: ${curriculum.gradeLevel}'),
            const SizedBox(height: 4),
            Text('Subjects: ${curriculum.subjects.join(', ')}'),
          ],
        ),
        trailing: const Icon(Icons.arrow_forward),
        onTap: () {
          // Navigate to detailed view if needed
        },
      ),
    );
  }
}
