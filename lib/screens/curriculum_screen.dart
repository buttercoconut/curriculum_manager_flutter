import 'package:flutter/material.dart';
import '../widgets/curriculum_card.dart';
import '../models/curriculum.dart';
import '../services/api_service.dart';

class CurriculumScreen extends StatefulWidget {
  const CurriculumScreen({Key? key}) : super(key: key);

  @override
  State<CurriculumScreen> createState() => _CurriculumScreenState();
}

class _CurriculumScreenState extends State<CurriculumScreen> {
  late Future<List<Curriculum>> _curriculums;

  @override
  void initState() {
    super.initState();
    _curriculums = ApiService.fetchCurriculums();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Curriculum List'),
      ),
      body: FutureBuilder<List<Curriculum>>(
        future: _curriculums,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          }
          final curriculums = snapshot.data ?? [];
          return ListView.builder(
            itemCount: curriculums.length,
            itemBuilder: (context, index) {
              return CurriculumCard(curriculum: curriculums[index]);
            },
          );
        },
      ),
    );
  }
}
