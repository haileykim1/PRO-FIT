package com.teamfour.myapplication

import android.app.ActionBar
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.Menu
import android.view.MenuItem
import android.widget.Toast
import com.teamfour.myapplication.databinding.ActivityBaseBinding

open class BaseActivity : AppCompatActivity() {

    companion object{
        private var backKeyPressedTime: Long = 0
    }

    override fun onCreateOptionsMenu(menu: Menu?): Boolean {
        menuInflater.inflate(R.menu.drawer, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.item1 -> {
                val intent = Intent(this, VirtualFittingActivity::class.java)
                startActivity(intent)
                true
            }
            R.id.item2 -> {
                val intent = Intent(this, ProfileActivity::class.java)
                startActivity(intent)
                true
            }
            /*R.id.item3 -> {
                val intent = Intent(this, ClothesActivity::class.java)
                startActivity(intent)
                true
            }*/
            else -> super.onContextItemSelected(item)
        }
    }

    @Override
    override fun onBackPressed() {


        if(System.currentTimeMillis() <= backKeyPressedTime + 2000){
            finishAffinity()
        }

        backKeyPressedTime = System.currentTimeMillis()
    }
}