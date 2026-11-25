# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Alpha
- Nhóm được chấm: 123

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | CPS 4.472 đ, chi phí toàn hệ thống 5.865 đ/yêu cầu so với 12.000 đ tự làm. Nhận diện kịch bản bất lợi khi xem lại 100%, CPS lên tới 12.415 đ (simulated) và đề xuất kiểm soát trong pilot. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Ghi nhãn simulated đầy đủ; giới hạn phạm vi nội địa và hàng nặng với CPS lần lượt 2.696 đ và 8.221 đ; loại quốc tế có CPS 22.515 đ và đối tác có tỉ lệ thành công thấp, 54,4%. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Phân nhóm ngẫu nhiên 20 nhân viên mỗi bên, tối thiểu 5.980 yêu cầu thực tế/nhóm, MDE 6 điểm, power mục tiêu 80%. Có luật dừng định lượng, người chịu trách nhiệm và rollback trong 30 phút. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện.

**Lý do:** Nhóm có đề xuất phù hợp với bằng chứng kinh tế, nhận diện các kịch bản bất lợi, thu hẹp phạm vi hợp lý và xây dựng pilot có đối chứng. Điều kiện là chấp thuận đánh đổi MDE 6 điểm, kiểm chứng chi phí nhân công thực tế, đảm bảo đủ cỡ mẫu và tuân thủ các luật dừng an toàn trước khi mở rộng.

**Một câu hỏi cho đội trình:** Nếu trong quá trình pilot, việc xem lại 100% khiến CPS tăng lên 12.415 đồng, vượt chi phí nhân viên tự làm, nhóm sẽ xử lý như thế nào để vừa đảm bảo hiệu quả kinh tế vừa duy trì an toàn?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm sẽ ưu tiên giảm thời gian xem lại và làm lại, đồng thời cải thiện chất lượng Agent. Chỉ giảm mức độ xem lại khi có bằng chứng an toàn và được phê duyệt. Nếu vẫn không đảm bảo hiệu quả kinh tế, nhóm sẽ thu hẹp phạm vi về nội địa hoặc tạm dừng pilot.