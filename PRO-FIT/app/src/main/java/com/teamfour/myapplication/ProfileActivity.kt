package com.teamfour.myapplication

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActivityProfileBinding

class ProfileActivity : BaseActivity() {

    val binding by lazy {ActivityProfileBinding.inflate(layoutInflater)}
    val userInfo = UserInfo()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(binding.root)

        setTitle("MY PROFILE")

        init()
    }

    private fun init(){
        binding.nameEdit.setText(userInfo.get(UserInfo.NAME)!!.toString())

        binding.setNameBtn.setOnClickListener {
            val newName = binding.nameEdit.text.toString()
            if(newName == ""){
                Toast.makeText(this, "정보를 입력해주세요", Toast.LENGTH_SHORT).show()
            }else{
                userInfo.set(UserInfo.NAME, newName)
                Toast.makeText(this, "변경되었습니다", Toast.LENGTH_SHORT).show()
            }
        }

    }
}