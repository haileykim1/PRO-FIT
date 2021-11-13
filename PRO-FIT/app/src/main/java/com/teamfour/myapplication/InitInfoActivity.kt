package com.teamfour.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActivityInitInfoBinding
import kotlinx.android.synthetic.main.activity_init_info.*

class InitInfoActivity : BaseActivity() {

    val binding by lazy {ActivityInitInfoBinding.inflate(layoutInflater)}

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        button.setOnClickListener{

            //이름, 신장 부분 입력했는지 확인.
            if((binding.nameEdit.text.isEmpty()) || (binding.heightEdit.text.isEmpty())){
                Toast.makeText(this, "초기 정보를 전부 입력해주세요", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }

            //정보 Local에 저장
            saveInfo(binding.nameEdit.text.toString(), binding.heightEdit.text.toString())
            //코드부분

            nextActivity()

        }

    }

    private fun saveInfo(name: String, height: String){
        val userInfo = UserInfo(this)
        userInfo.set(UserInfo.NAME, name)
        userInfo.set(UserInfo.NAME_PASSED, "true")
    }

    private fun nextActivity(){
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
        finish()
    }
}
