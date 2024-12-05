from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# MBTI问题集
QUESTIONS = [
    {
        "id": 1,
        "question": "在团队会议中，你通常会：",
        "options": [
            {"text": "积极发言，分享想法和观点", "type": "E", "score": 2},
            {"text": "先倾听他人，仔细思考后再发言", "type": "I", "score": 2}
        ]
    },
    {
        "id": 2,
        "question": "处理工作任务时，你更倾向于：",
        "options": [
            {"text": "关注具体细节和实际操作步骤", "type": "S", "score": 2},
            {"text": "思考整体策略和长期影响", "type": "N", "score": 2}
        ]
    },
    {
        "id": 3,
        "question": "在做项目决策时，你通常会：",
        "options": [
            {"text": "基于数据和逻辑进行分析", "type": "T", "score": 2},
            {"text": "考虑团队情绪和各方利益", "type": "F", "score": 2}
        ]
    },
    {
        "id": 4,
        "question": "面对工作计划，你倾向于：",
        "options": [
            {"text": "制定详细时间表并严格执行", "type": "J", "score": 2},
            {"text": "保持灵活，根据情况随时调整", "type": "P", "score": 2}
        ]
    },
    {
        "id": 5,
        "question": "在团队协作中，你更喜欢：",
        "options": [
            {"text": "主动协调，组织团队活动", "type": "E", "score": 2},
            {"text": "专注于自己的任务，独立完成", "type": "I", "score": 2}
        ]
    },
    {
        "id": 6,
        "question": "解决工作问题时，你更信赖：",
        "options": [
            {"text": "过往经验和已证实的方法", "type": "S", "score": 2},
            {"text": "创新思维和新的解决方案", "type": "N", "score": 2}
        ]
    },
    {
        "id": 7,
        "question": "处理同事间的矛盾时，你会：",
        "options": [
            {"text": "直接指出问题，寻求有效解决", "type": "T", "score": 2},
            {"text": "注重维护关系，寻求双方认可", "type": "F", "score": 2}
        ]
    },
    {
        "id": 8,
        "question": "管理项目进度时，你习惯：",
        "options": [
            {"text": "设定明确节点，按计划推进", "type": "J", "score": 2},
            {"text": "弹性安排，注重最终结果", "type": "P", "score": 2}
        ]
    },
    {
        "id": 9,
        "question": "在职场沟通中，你更擅长：",
        "options": [
            {"text": "通过会议和讨论交流想法", "type": "E", "score": 2},
            {"text": "通过邮件或文档表达观点", "type": "I", "score": 2}
        ]
    },
    {
        "id": 10,
        "question": "评估工作方案时，你更重视：",
        "options": [
            {"text": "实际可行性和具体收益", "type": "S", "score": 2},
            {"text": "创新程度和发展潜力", "type": "N", "score": 2}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS)

@app.route('/calculate', methods=['POST'])
def calculate_mbti():
    answers = request.json
    scores = {
        'E': 0, 'I': 0,
        'S': 0, 'N': 0,
        'T': 0, 'F': 0,
        'J': 0, 'P': 0
    }
    
    for answer in answers:
        question_id = answer['questionId']
        selected_option = answer['option']
        
        # 根据答案更新分数
        for question in QUESTIONS:
            if question['id'] == question_id:
                option = question['options'][selected_option]
                scores[option['type']] += option['score']
    
    # 计算最终类型
    mbti_type = ''
    mbti_type += 'E' if scores['E'] > scores['I'] else 'I'
    mbti_type += 'S' if scores['S'] > scores['N'] else 'N'
    mbti_type += 'T' if scores['T'] > scores['F'] else 'F'
    mbti_type += 'J' if scores['J'] > scores['P'] else 'P'
    
    # 获取性格类型描述
    descriptions = {
        'ISTJ': '物流师（Logistician）- 实际、有序的完美主义者。专注于系统和程序的建立与维护，以确保组织的高效运转。在工作中表现出极强的责任心和可靠性，善于制定详细的计划并一丝不苟地执行。重视传统和规则，追求稳定和可预测性。',
        'ISFJ': '守卫者（Defender）- 忠诚、谨慎的守护者。致力于维护传统和稳定，创造有序的工作环境。具有极强的观察力和记忆力，能够敏锐地察觉他人的需求。在团队中常常默默付出，是值得信赖的支柱。',
        'INFJ': '提倡者（Advocate）- 富有洞察力和创造力的理想主义者。善于发现他人潜力并推动积极变革。具有独特的远见卓识，能够将抽象的想法转化为切实可行的计划。追求完美，致力于实现更崇高的目标。',
        'INTJ': '建筑师（Architect）- 富有想象力的战略家。擅长构建创新的解决方案和长期战略规划。具有独立的思维方式和强大的分析能力，善于发现系统中的改进空间。追求卓越，不断探索新的可能性。',
        'ISTP': '鉴赏家（Virtuoso）- 大胆而实际的问题解决者。擅长在压力下快速分析情况并找到解决方案。具有极强的适应能力，善于利用现有资源解决具体问题。喜欢探索事物运作的原理，追求效率和实用性。',
        'ISFP': '探险家（Adventurer）- 灵活而艺术的探索者。善于在工作中寻找创新的实际解决方案。具有敏锐的审美感知能力，重视个人价值观和真实性。善于调和环境，创造和谐的氛围。',
        'INFP': '调停者（Mediator）- 富有同情心的创意思考者。追求真实和意义，善于调和不同观点。具有强烈的个人价值观和理想主义倾向，善于发现他人的潜力。在团队中起到桥梁作用，促进理解与和谐。',
        'INTP': '逻辑学家（Logician）- 创新的思考者。善于发现和解决复杂的逻辑问题，追求完美的解决方案。具有强大的分析能力和创造性思维，善于构建理论模型。对知识有着持续的渴求，不断探索新的可能性。',
        'ESTP': '企业家（Entrepreneur）- 聪明的问题解决者。善于把握机会，在紧急情况下表现出色。具有出色的观察力和行动力，能够快速适应环境变化。喜欢冒险和挑战，善于在实践中学习和成长。',
        'ESFP': '表演者（Entertainer）- 自发而热情的团队活力源。善于活跃团队氛围，创造积极的工作环境。具有天然的表现力和感染力，善于调动他人的积极性。注重当下，享受与他人合作的过程。',
        'ENFP': '竞选者（Campaigner）- 热情洋溢的创新者。善于激发他人潜能，推动创新项目的实施。具有出色的洞察力和创造力，善于发现新的可能性。充满好奇心和冒险精神，善于激励他人。',
        'ENTP': '辩论家（Debater）- 聪明而好奇的思想家。善于提出创新观点，挑战传统思维方式。具有敏锐的分析能力和创造性思维，善于发现问题的多个解决方案。喜欢智力挑战，追求思维的突破。',
        'ESTJ': '总经理（Executive）- 高效的管理者。善于建立和维护系统，确保目标的实现。具有出色的组织能力和执行力，重视规则和效率。善于制定清晰的目标和计划，并带领团队完成任务。',
        'ESFJ': '执政官（Consul）- 关心他人的团队协调者。善于创造和谐的工作环境，促进团队合作。具有强烈的责任心和服务意识，善于照顾他人的需求。重视传统和社会规范，追求稳定和和谐。',
        'ENFJ': '主人公（Protagonist）- 富有魅力的协调者。善于激励他人，推动团队发展和个人成长。具有天然的领导魅力和同理心，善于发现并培养他人的潜力。追求团队的共同发展和进步。',
        'ENTJ': '指挥官（Commander）- 大胆、具有想象力的领导者。善于制定战略、组织资源，推动组织发展。具有出色的决策能力和远见，善于发现机会并制定行动计划。追求效率和卓越，不断推动创新和变革。'
    }
    
    result = {
        'type': mbti_type,
        'description': descriptions.get(mbti_type, '未知类型'),
        'scores': scores
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)