import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/curriculum.dart';
import '../models/student.dart';
import '../models/grade.dart';

class ApiService {
  static const String baseUrl = 'http://localhost:8000/api';

  static Future<List<Curriculum>> fetchCurriculums() async {
    final response = await http.get(Uri.parse('$baseUrl/curriculums'));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((e) => Curriculum.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load curriculums');
    }
  }

  static Future<List<Student>> fetchStudents() async {
    final response = await http.get(Uri.parse('$baseUrl/students'));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((e) => Student.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load students');
    }
  }

  static Future<List<Grade>> fetchGrades() async {
    final response = await http.get(Uri.parse('$baseUrl/grades'));
    if (response.statusCode == 200) {
      final List<dynamic> data = jsonDecode(response.body);
      return data.map((e) => Grade.fromJson(e)).toList();
    } else {
      throw Exception('Failed to load grades');
    }
  }
}
